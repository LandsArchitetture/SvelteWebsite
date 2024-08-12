import axios from 'axios';
import { writable } from 'svelte/store';
import { readItems } from '@directus/sdk';
import { currentLanguage } from './language';

let allPostTranslations = {};
let allNavbarTranslations = {};

export const postTranslations = writable({});
export const navbarTranslations = writable({});
export const aboutUsTranslations = writable({});

export async function loadPostTranslations(directus) {
    const posts_translations = await directus.request(
        readItems('posts_translations', { limit: -1 })
    );

    allPostTranslations = posts_translations
}

export async function loadNavbarTranslations() {
    const navbar_translations = await axios.get('https://www.free-lands.com/Translations.json');

    allNavbarTranslations = navbar_translations.data;
}

export function updateLanguage() {
    let lang;

    currentLanguage.subscribe(value => lang = value);

    let navbarDict = {};
    let aboutUsDict = {};
    let postDict = {};

    for (const key in allNavbarTranslations['Navbar']) {
        navbarDict[key] = allNavbarTranslations['Navbar'][key][lang];
    }

    for (const key in allNavbarTranslations['AboutUs']) {
        aboutUsDict[key] = allNavbarTranslations['AboutUs'][key][lang];
    }

    allPostTranslations.forEach(post => {
        if (post.languages_id === lang) {
            postDict[post.posts_id] = post.text;
        }
    });

    postTranslations.set(postDict);
    navbarTranslations.set(navbarDict);
    aboutUsTranslations.set(aboutUsDict);
}
