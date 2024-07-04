<script>
	let translations = [
		{ id: 1, languages_id: 'en-US', text: 'Hello world' },
		{ id: 1, languages_id: 'it-IT', text: 'Ciao mondo' }
	];

	let language = 'en-US';

	let text = translations.find((t) => t.languages_id === language).text;

	function english() {
		language = 'en-US';
		let elem = document.getElementsByClassName('testo');
		console.log(elem);

		Array.from(elem).forEach((e) => {
			e.innerHTML = translations.find((t) => t.languages_id === language).text;
		});
	}

	function italian() {
		language = 'it-IT';
		let elem = document.getElementsByClassName('testo');
		console.log(elem);

		Array.from(elem).forEach((e) => {
			e.innerHTML = translations.find((t) => t.languages_id === language).text;
		});
	}
</script>

<button class="btn" on:click={english}>English</button>
<button class="btn" on:click={italian}>Italian</button>

<p class="testo">{text}</p>
<p class="testo">{text}</p>
<p class="testo">{text}</p>
<p class="testo">{text}</p>
