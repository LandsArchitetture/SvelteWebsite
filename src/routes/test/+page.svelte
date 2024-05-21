<script>
	let list = [
		{
			id: 'slide1',
			link: 'https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.jpg',
			prev: '#slide4',
			next: '#slide2'
		},
		{
			id: 'slide2',
			link: 'https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.jpg',
			prev: '#slide1',
			next: '#slide3'
		},
		{
			id: 'slide3',
			link: 'https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.jpg',
			prev: '#slide2',
			next: '#slide4'
		},
		{
			id: 'slide4',
			link: 'https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.jpg',
			prev: '#slide3',
			next: '#slide1'
		}
	];

	let list2 = [
		{
			id: 's1',
			link: 'https://img.daisyui.com/images/stock/photo-1625726411847-8cbb60cc71e6.jpg',
			prev: '#s4',
			next: '#s2'
		},
		{
			id: 's2',
			link: 'https://img.daisyui.com/images/stock/photo-1609621838510-5ad474b7d25d.jpg',
			prev: '#s1',
			next: '#s3'
		},
		{
			id: 's3',
			link: 'https://img.daisyui.com/images/stock/photo-1414694762283-acccc27bca85.jpg',
			prev: '#s2',
			next: '#s4'
		},
		{
			id: 's4',
			link: 'https://img.daisyui.com/images/stock/photo-1665553365602-b2fb8e5d1707.jpg',
			prev: '#s3',
			next: '#s1'
		}
	];
</script>

<button class="btn" onclick="my_modal_2.showModal()">open modal</button>

<button class="btn" onclick="my_modal_3.showModal()">open modal</button>

<dialog id="my_modal_3" class="modal">
	<div class="modal-box w-fit p-0">
		<div class="carousel w-fit">
			{#each list2 as l}
				<div id={l.id} class="carousel-item relative w-fit">
					<img src={l.link} class="w-full" alt="ciao" />
					<div
						class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2"
					>
						<a href={l.prev} class="btn btn-circle">❮</a>
						<a href={l.next} class="btn btn-circle">❯</a>
					</div>
				</div>
			{/each}
		</div>
		<form method="dialog">
			<button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
		</form>
	</div>
	<form method="dialog" class="modal-backdrop">
		<button>close</button>
	</form>
</dialog>

<dialog id="my_modal_2" class="modal">
	<div class="modal-box w-fit p-0">
		<div class="carousel w-fit">
			{#each list as l}
				<div id={l.id} class="carousel-item relative w-fit">
					<img src={l.link} class="w-full" alt="ciao" />
					<div
						class="absolute flex justify-between transform -translate-y-1/2 left-5 right-5 top-1/2"
					>
						<a href={l.prev} class="btn btn-circle">❮</a>
						<a href={l.next} class="btn btn-circle">❯</a>
					</div>
				</div>
			{/each}
		</div>
		<form method="dialog">
			<button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
		</form>
	</div>
	<form method="dialog" class="modal-backdrop">
		<button>close</button>
	</form>
</dialog>
