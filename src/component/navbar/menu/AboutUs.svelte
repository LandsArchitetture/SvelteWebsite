<script>
	import { get } from 'svelte/store';

	export let language;
	export let translations;
	/**
	 * Open the About Us modal when called
	 */
	function openModal() {
		let index = 0;
		const modal = document.getElementById('AboutUs');
		const carousel = document.getElementById('carousel.AboutUs');
		const image = document.getElementById('img.AboutUs.' + index);

		if (window.innerWidth > image.width) {
			carousel.style.maxWidth = image.width + 'px';
			carousel.style.maxHeight = image.height + 'px';
		} else {
			carousel.style.maxWidth = window.innerWidth + 'px';
			carousel.style.maxHeight = (2 * window.innerWidth) / 3 + 'px';
		}

		modal.showModal();

		window.location.hash = '';
		window.location.hash = '#AboutUs.' + index;
	}

	let currentLanguage = language;

	$: if (currentLanguage !== language) {
		document.getElementById('aboutUs').innerHTML = getTranslation('About us');
		currentLanguage = language;
	}

	function getTranslation(word) {
		if (translations && translations[word]) {
			return translations[word][language];
		}
		return '';
	}
</script>

<button class="font-bold" on:click={openModal} id="aboutUs">About Us</button>
