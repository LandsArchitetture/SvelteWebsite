<script>
    import { getContext } from 'svelte';

    export let image;
    export let location;
    export let date;
    export let id;
    export let language = 'en-US';
    export let link = '';

    const URL = 'https://www.free-lands.com/';

    const BLACK = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/A_black_image.jpg/800px-A_black_image.jpg'

    let src = URL + image + '_modal.jpeg';

    function handleError(event){
        event.target.src = BLACK;
    }

    let text = getContext('translations').filter(translation => translation.posts_id === id && translation.languages_id === language).text;

</script>

<div class="element">
    <img class="image" src="{src}" alt="{location}" onerror={handleError}>
    <div class="info">
        <h3 class="location">{location}</h3>
        <p class="date">{date}</p>
        <a class="description" href="{link}">{text}</a>
    </div>
</div>