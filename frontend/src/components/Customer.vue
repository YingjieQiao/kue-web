
<template>
  <div>
    <p>Waiting for your food</p>
    <p>ETA: {{ order }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      order: 0
    }
  },
  methods: {
    getOrder () {
      this.order = this.getOrderFromBackend()
    },
    getOrderFromBackend () {
      const path = `http://localhost:5000/api/getOrder`
      axios.get(path)
      .then(response => {
        this.order = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getOrder()
  }
}
</script>
