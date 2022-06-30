import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
          light: {
            secondary: '#f5f5f5',
          },
          dark: {
            secondary: '#424242',
          },
        },
      },
});
