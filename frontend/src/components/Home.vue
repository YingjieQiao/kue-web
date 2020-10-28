
<template>
  <div>
    <p>Home page</p>
    <p>Order: {{ order }}</p>
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
      const path = `http://localhost:5000/api/random`
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
