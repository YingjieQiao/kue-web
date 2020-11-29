
<template>
  <div>
    <p>Waiting for your food</p>
    <p>order placed at: {{ order["order time"] }}</p>
    <p>ETA: {{ order["eta"] }}</p>
    <p>Please refresh the webpage to see any updates of your food!</p>
    
    <p>Please enter your rating below on a scale of 1 - 5</p>
    <input v-model="rating" placeholder="5 for best">
    <button @click="postRating"> click to send your rating! </button>
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      order: 0,
      rating: 0
    }
  },
  methods: {
    getOrder () {
      this.order = this.getOrderFromBackend()
    },
    getOrderFromBackend () {
      const path = process.env.API_URL + '/getOrder' // `http://localhost:5000/api/getOrder`
      axios.post(path, {order_id: this.$route.params.order_id, username: this.$route.params.username})
      .then(response => {
        this.order = response.data
      })
      .catch(error => {
        console.log(error)
      })
    },
    postRating: function (event) {
      const path = process.env.API_URL + '/postRating'
      axios.post(path, {order_id: this.$route.params.order_id, username: this.$route.params.username, rating: this.rating})
      .catch(error => {
        console.log(error)
      })
      alert('Rating posted!')
    }
  },
  created () {
    this.getOrder()
  }
}
</script>
