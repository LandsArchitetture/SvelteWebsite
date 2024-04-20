<script>
	import ModalElement from "./ModalElement.svelte";

    export let data;

    export let post;

    const URL = 'https://www.free-lands.com/';

    let related = data.posts.filter(p => p.project === post.project);

    let index = related.findIndex(p => p.id === post.id);

</script>

<button class="brick {post.size} p-0 border-0 rounded-xl hover:shadow-[0_0_20px_10px_rgba(0,0,0,0.7)] overflow-hidden" on:click={()=>{window.history.replaceState(null, document.title, '#' + post.project + '.' + index);document.getElementById(post.project).showModal()}}>
    <img id={post.id + '_' + post.size} class="object-cover w-full" loading="lazy" src="{URL + post.image + '_' + post.size + '.jpeg'}" alt="{post.project}"/>
    <p class="project text-white [text-shadow:_0_0_5px_rgb(0_0_0)] absolute top-0 left-2 text-xl font-bold">{post.project}</p>
    <p class="date text-white [text-shadow:_0_0_5px_rgb(0_0_0)] absolute bottom-0 right-2 text-sm">{post.date}</p>
</button>

<dialog id={post.project} class="modal">
    <div class="modal-box w-fit max-w-fit p-0">
        <!-- Carousel -->
        <ModalElement post={post} related={related}/>
        <!-- Close button -->
        <form method="dialog">
            <button class="btn btn-sm btn-circle btn-ghost absolute right-4 top-4 text-red-700 scale-150 [text-shadow:_0_0_5px_rgb(0_0_0)]">✕</button>
        </form>
        <!-- Header -->
        <p class="modalHeader text-white absolute top-4 left-4 font-bold text-3xl [text-shadow:_0_0_5px_rgb(0_0_0)] select-none">{post.project ? post.project : ''}</p>
        <!-- Carousel -->
    </div>
    <!-- Close when click outside -->
    <form method="dialog" class="modal-backdrop">
        <button></button>
    </form>
</dialog>