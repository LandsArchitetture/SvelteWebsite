<script>
    export let id;

    const URL = 'https://www.free-lands.com/';

    let post = getContext('posts').data.find(post => post.id === id);

    let image = URL + post.image + '_' + post.size + '.jpeg';
    let project = post.project;
    let size = post.size;

    function toggleModal() {
        let display = document.getElementById(project).style.display;
        if (display === 'none') document.getElementById(project).style.display = 'block';
        else document.getElementById(project).style.display = 'none';
    }

</script>


<button class="brick {size}" onclick={toggleModal}>
    <img src="{image}" alt="{project}" />
</button>

<dialog id={project} class="modal">
    <div class="modal-content">
        <span class="close" onclick={toggleModal}>&times;</span>
        <img src="{image}" alt="{project}" />
    </div>
    <form method="dialog" class="modal-backdrop">
        <button>Close</button>
    </form>
</dialog>


    
