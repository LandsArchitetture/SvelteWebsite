<script>
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
</script>

<button class="font-bold" on:click={openModal}>About Us</button>
