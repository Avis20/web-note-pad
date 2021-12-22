<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Ping',
    data() {
      return {
        msg: '',
      }
    },
    methods: {
      getMessage() {
        axios.get('/')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.log(error);
        })
      }
    },
    created() {
      this.getMessage()
    }
  }

</script>
