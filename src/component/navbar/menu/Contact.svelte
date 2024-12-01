<script>
	import { navbarTranslations } from '$lib/stores/translations';
	/**
	 * Open the Contact modal when called
	 */
	function showModal() {
		document.getElementById('Contact').showModal();
	}
</script>

<button class="font-bold" on:click={showModal} id="cont"
	>{$navbarTranslations['Contact'] ? navbarTranslations['Contact'] : ''}</button
>
