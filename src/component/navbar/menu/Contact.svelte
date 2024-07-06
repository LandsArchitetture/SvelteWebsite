<script>
	export let language;
	export let translations;
	/**
	 * Open the Contact modal when called
	 */
	function showModal() {
		document.getElementById('Contact').showModal();
	}

	let currentLanguage = language;

	$: if (currentLanguage !== language) {
		document.getElementById('cont').innerHTML = getTranslation('Contact');
		currentLanguage = language;
	}

	function getTranslation(word) {
		if (translations && translations[word]) {
			return translations[word][language];
		}
		return '';
	}
</script>

<button class="font-bold" on:click={showModal} id="cont">Contact</button>
