<?php
/**
 * Ioana Balan Child - functions.php
 *
 * Child theme pentru Hello Elementor. Face exact cinci lucruri:
 * incarca stilurile parinte + copil, preincarca cele patru fonturi critice,
 * dezactiveaza Google Fonts si documenteaza decizia despre SVG.
 *
 * Tot ce inseamna layout, culoare si tipografie traieste in
 * Elementor > Setari site, nu aici.
 *
 * @package ioana-balan-child
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * 1. Stiluri: parintele intai, copilul dependent de el.
 *
 * Copilul e versionat cu filemtime() ca sa sparga cache-ul la fiecare
 * modificare reala a fisierului, fara sa umblam la numarul de versiune.
 */
function ib_child_enqueue_styles() {
	wp_enqueue_style(
		'hello-elementor-parent',
		get_template_directory_uri() . '/style.css',
		array(),
		wp_get_theme( get_template() )->get( 'Version' )
	);

	$child_style = get_stylesheet_directory() . '/style.css';

	wp_enqueue_style(
		'ioana-balan-child',
		get_stylesheet_directory_uri() . '/style.css',
		array( 'hello-elementor-parent' ),
		file_exists( $child_style ) ? filemtime( $child_style ) : '1.0.0'
	);
}
add_action( 'wp_enqueue_scripts', 'ib_child_enqueue_styles', 20 );

/**
 * 2. Preload doar pentru fonturile din primul ecran.
 *
 * Inter 400 = body, EB Garamond 500 = titluri. Subseturile latin-ext
 * sunt necesare pentru diacriticele romanesti (a-breve, s-virgula, t-virgula).
 * Restul de opt fisiere se incarca la cerere - preload-ul lor ar concura
 * cu acestea pentru banda de la inceputul incarcarii.
 */
function ib_child_preload_fonts() {
	$fonts = array(
		'inter-400-latin.woff2',
		'inter-400-latin-ext.woff2',
		'eb-garamond-500-latin.woff2',
		'eb-garamond-500-latin-ext.woff2',
	);

	$base = get_stylesheet_directory_uri() . '/assets/fonts/';

	foreach ( $fonts as $font ) {
		printf(
			'<link rel="preload" as="font" type="font/woff2" href="%s" crossorigin>' . "\n",
			esc_url( $base . $font )
		);
	}
}
add_action( 'wp_head', 'ib_child_preload_fonts', 1 );

/**
 * 3a. Elementor nu mai tipareste link-uri catre Google Fonts.
 */
add_filter( 'elementor/frontend/print_google_fonts', '__return_false', 10 );

/**
 * 3b. Orice alt stil inregistrat cu src catre Google Fonts se scoate din coada.
 *
 * Prioritatea 100 ruleaza dupa ce plugin-urile si-au inregistrat stilurile.
 */
function ib_child_dequeue_google_fonts() {
	$styles = wp_styles();

	if ( ! $styles || empty( $styles->registered ) ) {
		return;
	}

	foreach ( $styles->registered as $handle => $style ) {
		if ( empty( $style->src ) ) {
			continue;
		}

		if ( false !== strpos( $style->src, 'fonts.googleapis.com' )
			|| false !== strpos( $style->src, 'fonts.gstatic.com' ) ) {
			wp_dequeue_style( $handle );
			wp_deregister_style( $handle );
		}
	}
}
add_action( 'wp_enqueue_scripts', 'ib_child_dequeue_google_fonts', 100 );

/**
 * 3c. Fara preconnect / dns-prefetch catre domeniile Google Fonts.
 *
 * WordPress accepta doua forme in lista de resource hints: string simplu
 * sau array cu cheia 'href'. Le tratam pe amandoua.
 *
 * @param array  $urls          Lista de resurse pentru relatia data.
 * @param string $relation_type Tipul relatiei (preconnect, dns-prefetch, ...).
 * @return array Lista filtrata.
 */
function ib_child_filter_resource_hints( $urls, $relation_type ) {
	if ( ! in_array( $relation_type, array( 'preconnect', 'dns-prefetch' ), true ) ) {
		return $urls;
	}

	foreach ( $urls as $key => $url ) {
		$href = '';

		if ( is_array( $url ) && isset( $url['href'] ) ) {
			$href = $url['href'];
		} elseif ( is_string( $url ) ) {
			$href = $url;
		}

		if ( '' === $href ) {
			continue;
		}

		if ( false !== strpos( $href, 'fonts.googleapis.com' )
			|| false !== strpos( $href, 'fonts.gstatic.com' ) ) {
			unset( $urls[ $key ] );
		}
	}

	return array_values( $urls );
}
add_filter( 'wp_resource_hints', 'ib_child_filter_resource_hints', 10, 2 );

/**
 * 4. SVG pentru logo: se activeaza prin pluginul Safe SVG, NU prin cod aici.
 *
 * Adaugarea 'image/svg+xml' in upload_mimes din tema deschide incarcarea de
 * SVG nesanitizat pentru orice utilizator care poate incarca fisiere - un
 * SVG poate contine JavaScript. Safe SVG sanitizeaza fisierul la incarcare.
 * Decizia ramane la nivel de plugin, ca sa poata fi dezactivata fara sa
 * atinga tema.
 */
