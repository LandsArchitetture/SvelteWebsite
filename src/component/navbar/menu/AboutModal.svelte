<script>
	import { aboutUsTranslations } from '$lib/stores/translations';

	const BLACK =
		'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg';

	const KEYWORDS = [
		{
			word: 'Environment',
			image: BLACK,
			prev: 'AboutUs.0',
			next: 'AboutUs.2',
			id: 'AboutUs.1',
			text: 'We build it, consciously or not, every day. It was once called Nature.'
		},
		{
			word: 'Architecture',
			image: BLACK,
			prev: 'AboutUs.1',
			next: 'AboutUs.3',
			id: 'AboutUs.2',
			text: 'Every definition of architecture today is obsolete and every attempt to harness it in codes. Architecture can only be researched. Sometimes it offers itself, for a strange set of circumstances, others it escapes.'
		},
		{
			word: 'City',
			image: BLACK,
			prev: 'AboutUs.2',
			next: 'AboutUs.4',
			id: 'AboutUs.3',
			text: 'Is a collection of buildings and citizens. It takes both to make a living city.'
		},
		{
			word: 'Competitions',
			image: BLACK,
			prev: 'AboutUs.3',
			next: 'AboutUs.5',
			id: 'AboutUs.4',
			text: 'Are useful project tools, if their purpose is not ideological.'
		},
		{
			word: 'Construction',
			image: BLACK,
			prev: 'AboutUs.4',
			next: 'AboutUs.6',
			id: 'AboutUs.5',
			text: 'Is the technological ability to think and develop projects. The true knowledge of the architect.'
		},
		{
			word: 'Culture',
			image: BLACK,
			prev: 'AboutUs.5',
			next: 'AboutUs.7',
			id: 'AboutUs.6',
			text: 'Is the care, of the Earth, on which we live. But do we still have an Earth culture?'
		},
		{
			word: 'Economy',
			image: BLACK,
			prev: 'AboutUs.6',
			next: 'AboutUs.8',
			id: 'AboutUs.7',
			text: 'Still and always the house ... it is the DNA of our times.'
		},
		{
			word: 'Edifice',
			image: BLACK,
			prev: 'AboutUs.7',
			next: 'AboutUs.9',
			id: 'AboutUs.8',
			text: "Is the construction of man's dwelling on Earth. In a landscape. Each building is unique."
		},
		{
			word: 'Building',
			image: BLACK,
			prev: 'AboutUs.8',
			next: 'AboutUs.10',
			id: 'AboutUs.9',
			text: 'Is the complex of human activities related to the construction of buildings.'
		},
		{
			word: 'Hybrid',
			image: BLACK,
			prev: 'AboutUs.9',
			next: 'AboutUs.11',
			id: 'AboutUs.10',
			text: 'Is the state of affairs of the contemporary world. Architecture is hybrid, never pure. The construction as well.'
		},
		{
			word: 'Innovation',
			image: BLACK,
			prev: 'AboutUs.10',
			next: 'AboutUs.12',
			id: 'AboutUs.11',
			text: 'Could it be our personal ability to respond to real problems?'
		},
		{
			word: 'Landscape',
			image: BLACK,
			prev: 'AboutUs.11',
			next: 'AboutUs.13',
			id: 'AboutUs.12',
			text: "It was not there before, now it is determined by man's footprints on Earth and by his gaze."
		},
		{
			word: 'Projects',
			image: BLACK,
			prev: 'AboutUs.12',
			next: 'AboutUs.14',
			id: 'AboutUs.13',
			text: 'Are a look ahead and therefore the process that leads to the construction of an artifact. Without a vision of the world, one cannot design.'
		},
		{
			word: 'Renovations',
			image: BLACK,
			prev: 'AboutUs.13',
			next: 'AboutUs.15',
			id: 'AboutUs.14',
			text: 'Is the remodeling of an artifact. The main activity of the 21st century. Renovating the buildings, the city ... the whole world.'
		},
		{
			word: 'Valuation',
			image: BLACK,
			prev: 'AboutUs.14',
			next: 'AboutUs.16',
			id: 'AboutUs.15',
			text: 'Is the giving of value to things and turning them into money. Strength without which it makes no sense to talk about this profession.'
		},
		{
			word: 'Society',
			image: BLACK,
			prev: 'AboutUs.15',
			next: 'AboutUs.17',
			id: 'AboutUs.16',
			text: 'Today is the largest transformation taking place since the Neolithic. But has man always been the same?'
		},
		{
			word: 'Technique',
			image: BLACK,
			prev: 'AboutUs.16',
			next: 'AboutUs.18',
			id: 'AboutUs.17',
			text: 'Is the quality of our daily life. Our DNA is technical. We live technically.'
		},
		{
			word: '3333',
			image: BLACK,
			prev: 'AboutUs.17',
			next: 'AboutUs.0',
			id: 'AboutUs.18',
			text: 'Our first project for a low-cost residential building. Architecture for everyone!'
		}
	];

	/**
	 * Set the size of the carousel according to the image size
	 * @param dir The direction of the carousel (1 for next, -1 for previous)
	 */
	function setSize(dir) {
		let carousel = document.getElementById('carousel.AboutUs');
		let index = Number(window.location.href.split('#')[1].split('.')[1]);

		index = index + dir;
		if (index < 0) index = KEYWORDS.length - 1;
		if (index >= KEYWORDS.length) index = 0;

		let image = document.getElementById('img.AboutUs.' + index);

		if (window.innerWidth > image.width) {
			carousel.style.maxWidth = image.width + 'px';
			carousel.style.maxHeight = image.height + 'px';
		} else {
			carousel.style.maxWidth = window.innerWidth + 'px';
			carousel.style.maxHeight = (2 * image.width) / 3 + 'px';
		}
	}

	/**
	 * Handle the resize of the carousel when called
	 * @param dir The direction of the carousel (1 for next, -1 for previous)
	 */
	function handleSetSize(dir) {
		return (event) => {
			setSize(dir);
		};
	}
</script>

<dialog id="AboutUs" class="modal p-0 !bg-transparent">
	<div class="modal-box absolute flex p-0 w-fit max-w-fit max-h-fit select-none">
		<!-- Carousel -->
		<div
			id="carousel.AboutUs"
			class="carousel relative transition-all duration-200 lg:max-w-[900px] max-h-fit max-w-screen flex w-fit"
		>
			<!-- Emanuele Slide -->
			<div id="AboutUs.0" class="carousel-item relative w-fit">
				<img
					id={'img.' + 'AboutUs.0'}
					src="$lib/img/EmanueleSaurwein.jpg"
					alt={'Emanuele Saurwein'}
					class="w-[900px] h-[600px] object-cover"
				/>
				<p class="absolute bottom-[75px] left-[25px] text-white text-lg uppercase">
					{'Emanuele Saurwein'}
				</p>
				<p class="absolute bottom-[50px] left-[25px] text-white capitalize">
					{$aboutUsTranslations['Profession']}
				</p>
				<p class="absolute bottom-[25px] left-[25px] text-white">
					{$aboutUsTranslations['Description']}
				</p>
				<p
					class="absolute top-1/2 -translate-y-1/2 right-[75px] w-2/5 text-white"
					id="Introduction"
				>
					{$aboutUsTranslations['Introduction']}
				</p>

				<div class="absolute flex justify-between -translate-y-1/2 left-5 right-5 top-1/2">
					<a href={'#' + 'AboutUs.18'} on:click={handleSetSize(-1)} class="btn btn-circle">❮</a>
					<a href={'#' + 'AboutUs.1'} on:click={handleSetSize(1)} class="btn btn-circle">❯</a>
				</div>
			</div>
			<!-- Keyword Slides -->
			{#each KEYWORDS as keyword, i}
				<div id={keyword.id} class="carousel-item relative w-fit">
					<img
						id={'img.' + keyword.id}
						src={keyword.image}
						alt={keyword.word}
						class="w-full h-full"
					/>
					<p
						id={keyword.word}
						class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-white text-center text-4xl p-2 uppercase"
					>
						{$aboutUsTranslations[keyword.word]}
					</p>
					<p id={i} class="absolute bottom-[25px] left-1/2 -translate-x-1/2 text-white text-center">
						{$aboutUsTranslations[i + 1]}
					</p>
					<div
						class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2"
					>
						<a href={'#' + keyword.prev} on:click={handleSetSize(-1)} class="btn btn-circle">❮</a>
						<a href={'#' + keyword.next} on:click={handleSetSize(1)} class="btn btn-circle">❯</a>
					</div>
				</div>
			{/each}
		</div>
		<!-- Close button -->
		<form method="dialog">
			<button
				class="btn btn-sm btn-circle btn-ghost absolute right-4 top-4 text-red-700 text-2xl [text-shadow:_0_0_5px_rgb(0_0_0)]"
				>✕</button
			>
		</form>
		<!-- Header -->
	</div>
	<!-- Close when click outside -->
	<form method="dialog" class="modal-backdrop">
		<button class="w-screen h-screen">✕</button>
	</form>
</dialog>
