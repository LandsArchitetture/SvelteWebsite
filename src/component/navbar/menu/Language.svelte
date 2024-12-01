<script>
	import { currentLanguage } from '$lib/stores/language';
	import { updateLanguage, navbarTranslations } from '$lib/stores/translations';

	function changeLanguage(lang) {
		let language;
		currentLanguage.subscribe((value) => (language = value));
		if (lang === language) return;
		currentLanguage.set(lang);
		updateLanguage();
	}
</script>

<details>
	<summary class="font-bold" id="lang"
		>{$navbarTranslations['Language'] ? navbarTranslations['Language'] : ''}</summary
	>
	<ul
		class="menu font-bold p-2 lg:bg-base-300 bg-base-200 rounded-t-none -z-5 lg:shadow-[5px_5px_2px_0_rgba(0,0,0,0.5)]"
	>
		<li><button on:click={() => changeLanguage('en-US')}>English</button></li>
		<li><button on:click={() => changeLanguage('it-IT')}>Italiano</button></li>
	</ul>
</details>
