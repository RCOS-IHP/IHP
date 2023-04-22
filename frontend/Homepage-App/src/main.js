import { createApp } from 'vue';
import App from './App.vue';

// Font Awesome imports
import { library } from '@fortawesome/fontawesome-svg-core';
import { faFacebookF, faTwitter, faLinkedinIn, faYoutube } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// Add the imported icons to the Font Awesome library
library.add(faFacebookF, faTwitter, faLinkedinIn, faYoutube);

// Create the Vue app
const app = createApp(App);

// Register the Font Awesome component globally
app.component('font-awesome-icon', FontAwesomeIcon);

// Mount the app
app.mount('#app');
