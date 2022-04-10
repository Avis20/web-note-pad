<!-- ./frontend/src/components/HelloWorld.vue -->

<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PingMsg',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      // при вызове метода, делаем запрос на backend за получением данных
      axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        })
    },
  },
  created() {
    // При создании компонента вызываем getMessage
    this.getMessage();
  }
};
</script>

