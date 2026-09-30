<?php
/**
 * Migrarea celor 28 de pagini din zone-mockup in Elementor.
 * Se incarca din execute-php (Novamira): include WP_CONTENT_DIR.'/novamira-sandbox/migrare/lib.inc';
 * Sursa JSON: branch-ul migrare-elementor din laur2198/ioana-balan (generat de migrare/convert.py).
 * Toate paginile se creeaza/actualizeaza ca DRAFT. Nu publica nimic.
 */

const IB_MIG_RAW    = 'https://raw.githubusercontent.com/laur2198/ioana-balan/migrare-elementor/migrare/out/';
const IB_MIG_BACKUP = '/home/grandmusic/_novamira-backups/migrare-28-pagini/';

function ib_mig_fetch( $name ) {
	$r = wp_remote_get( IB_MIG_RAW . $name . '?t=' . time(), array( 'timeout' => 30 ) );
	if ( is_wp_error( $r ) || 200 !== wp_remote_retrieve_response_code( $r ) ) {
		throw new Exception( 'fetch esuat: ' . $name );
	}
	return wp_remote_retrieve_body( $r );
}

/** baza fisierului din prototip -> ID atasament din Media Library (ex. ioana-balan-scena-costum-rosu -> 3807) */
function ib_mig_att( $base ) {
	static $cache = array();
	if ( isset( $cache[ $base ] ) ) {
		return $cache[ $base ];
	}
	global $wpdb;
	$like = $wpdb->esc_like( '/' . $base ) . '-%';
	$id   = $wpdb->get_var( $wpdb->prepare(
		"SELECT post_id FROM {$wpdb->postmeta} WHERE meta_key='_wp_attached_file' AND CONCAT('/',meta_value) LIKE %s ORDER BY post_id DESC LIMIT 1",
		'%' . $like
	) );
	if ( ! $id ) {
		throw new Exception( 'imagine lipsa din Media Library: ' . $base );
	}
	return $cache[ $base ] = (int) $id;
}

/** Inlocuieste {{IMG:x}} / {{IMGID:x}} si pune srcset pe <img data-ib-img>. */
function ib_mig_resolve( $els ) {
	$walk = function ( &$v ) use ( &$walk ) {
		if ( is_array( $v ) ) {
			foreach ( $v as $k => &$x ) {
				if ( is_string( $x ) && preg_match( '/^\{\{IMGID:([a-z0-9-]+)\}\}$/', $x, $m ) ) {
					$x = ib_mig_att( $m[1] );
				} else {
					$walk( $x );
				}
			}
			return;
		}
		if ( ! is_string( $v ) || false === strpos( $v, '{{IMG' ) ) {
			return;
		}
		$v = preg_replace_callback( '/<img([^>]*?)data-ib-img="([a-z0-9-]+)"([^>]*)>/', function ( $m ) {
			$id  = ib_mig_att( $m[2] );
			$set = wp_get_attachment_image_srcset( $id, 'full' );
			$img = '<img' . $m[1] . $m[3] . '>';
			if ( $set ) {
				$img = str_replace( '<img', '<img srcset="' . esc_attr( $set ) . '" sizes="(max-width: 767px) 100vw, 1200px"', $img );
			}
			return $img;
		}, $v );
		$v = preg_replace_callback( '/\{\{IMG:([a-z0-9-]+)\}\}/', function ( $m ) {
			return wp_get_attachment_url( ib_mig_att( $m[1] ) );
		}, $v );
	};
	$walk( $els );
	return $els;
}

/** zone.css in child theme + enqueue conditionat de meta _ib_tw (doar paginile migrate). */
function ib_mig_install_css() {
	$dir = get_stylesheet_directory();
	$css = ib_mig_fetch( 'zone.css' );
	if ( ! is_dir( IB_MIG_BACKUP ) ) {
		wp_mkdir_p( IB_MIG_BACKUP );
	}
	if ( file_exists( $dir . '/assets/zone.css' ) ) {
		copy( $dir . '/assets/zone.css', IB_MIG_BACKUP . 'zone.css.' . date( 'Ymd-His' ) );
	}
	file_put_contents( $dir . '/assets/zone.css', $css );

	$fn = $dir . '/functions.php';
	$src = file_get_contents( $fn );
	$out = array( 'css_bytes' => strlen( $css ), 'enqueue' => 'exista' );
	if ( false === strpos( $src, 'ib_child_zone_css' ) ) {
		copy( $fn, IB_MIG_BACKUP . 'functions.php.' . date( 'Ymd-His' ) );
		$snippet = <<<'PHP'


/* ---- Paginile migrate din zone-mockup: utilitare Tailwind scopate pe .ib-tw ----
   Se incarca doar pe paginile cu meta _ib_tw (cele 28 de pagini noi). */
function ib_child_zone_css() {
	if ( ! is_singular() || ! get_post_meta( get_queried_object_id(), '_ib_tw', true ) ) {
		return;
	}
	$dir = get_stylesheet_directory();
	wp_enqueue_style( 'ib-child-zone', get_stylesheet_directory_uri() . '/assets/zone.css', array( 'ib-child-blocks' ), filemtime( $dir . '/assets/zone.css' ) );
}
add_action( 'wp_enqueue_scripts', 'ib_child_zone_css', 31 );
PHP;
		file_put_contents( $fn, $src . $snippet );
		$out['enqueue'] = 'adaugat';
	}
	exec( 'php -l ' . escapeshellarg( $fn ) . ' 2>&1', $lint );
	$out['lint'] = implode( ' ', $lint );
	return $out;
}

function ib_mig_find( $src ) {
	$q = get_posts( array( 'post_type' => 'page', 'post_status' => 'any', 'meta_key' => '_ib_src', 'meta_value' => $src, 'numberposts' => 1, 'fields' => 'ids' ) );
	return $q ? (int) $q[0] : 0;
}

/** Creeaza sau actualizeaza o pagina din migrare/out/<name>.json. Mereu draft. */
function ib_mig_page( $name ) {
	$data = json_decode( ib_mig_fetch( $name . '.json' ), true );
	if ( ! $data ) {
		throw new Exception( 'JSON invalid: ' . $name );
	}
	$m   = $data['meta'];
	$els = ib_mig_resolve( $data['elements'] );

	$parent = 0;
	if ( $m['parent'] ) {
		$parent = ib_mig_find( $m['parent'] . '.html' );
		if ( ! $parent ) {
			throw new Exception( 'hub-ul trebuie creat inaintea zonelor' );
		}
	}

	$id  = ib_mig_find( $m['src'] );
	$new = ! $id;
	if ( $new ) {
		$id = wp_insert_post( array(
			'post_type'   => 'page',
			'post_status' => 'draft',
			'post_title'  => $m['title'],
			'post_name'   => $m['slug'],
			'post_parent' => $parent,
		), true );
		if ( is_wp_error( $id ) ) {
			throw new Exception( $id->get_error_message() );
		}
		update_post_meta( $id, '_ib_src', $m['src'] );
	} else {
		if ( ! is_dir( IB_MIG_BACKUP ) ) {
			wp_mkdir_p( IB_MIG_BACKUP );
		}
		file_put_contents( IB_MIG_BACKUP . $m['slug'] . '-' . $id . '-' . date( 'Ymd-His' ) . '.json', get_post_meta( $id, '_elementor_data', true ) );
		if ( 'draft' !== get_post_status( $id ) ) {
			throw new Exception( "pagina $id nu mai e draft; nu o suprascriu" );
		}
	}

	update_post_meta( $id, '_elementor_edit_mode', 'builder' );
	update_post_meta( $id, '_elementor_template_type', 'wp-page' );
	update_post_meta( $id, '_wp_page_template', 'elementor_header_footer' );
	update_post_meta( $id, '_ib_tw', 1 );

	$doc = \Elementor\Plugin::$instance->documents->get( $id, false );
	$doc->save( array( 'elements' => $els, 'settings' => array( 'template' => 'elementor_header_footer' ) ) );
	if ( 'draft' !== get_post_status( $id ) ) {
		wp_update_post( array( 'ID' => $id, 'post_status' => 'draft' ) );
	}

	// SEO: title/meta din prototip; noindex pe zonele fara locatii; JSON-LD pastrat pentru etapa de schema
	update_post_meta( $id, '_yoast_wpseo_title', $m['seo_title'] );
	update_post_meta( $id, '_yoast_wpseo_metadesc', $m['metadesc'] );
	if ( $m['noindex'] ) {
		update_post_meta( $id, '_yoast_wpseo_meta-robots-noindex', '1' );
	}
	update_post_meta( $id, '_ib_jsonld', wp_slash( wp_json_encode( $m['jsonld'], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES ) ) );

	// lectiile din 9 sept.: CSS regenerat per document, cache-ul de element golit
	delete_post_meta( $id, '_elementor_element_cache' );
	\Elementor\Core\Files\CSS\Post::create( $id )->update();

	return array( 'id' => $id, 'new' => $new, 'status' => get_post_status( $id ), 'slug' => get_post_field( 'post_name', $id ), 'parent' => $parent );
}
