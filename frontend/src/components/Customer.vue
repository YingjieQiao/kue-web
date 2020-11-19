
<template>
  <div>
    <p>Waiting for your food</p>
    <p>ETA: {{ order }}</p>
  </div>
</template>

<script>
import axios from 'axios'

// const formData = new FormData()
// formData.append('username', this.$route.params.username)
// formData.append('id', this.$route.params.id)

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
      axios.post(path, {order_id: this.$route.params.order_id, username: this.$route.params.username})
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
