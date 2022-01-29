<template>
  <div>
    <h1>Home</h1>
    <button @click="submit">submit</button>

    <div class="response">
      {{response}}
    </div>

    <ul id="example-1">
      <li v-for="company in companies" :key="company.id">
        {{ company.name }}
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios';
  
  export default {
    
    props: ['category'],
    async mounted() {
      const companies = await axios.get(`${this.$config.apiUrl}/companies`);
      if (companies.data) {
        console.log(companies.data)
        this.companies = companies.data;
      }
    },
    
    data() {
      return {
        companies: null,
        response: null
      }
    },

    methods: {
      async submit(event) {
        console.log(event);
        let resp = await axios.post(this.$config.vgsInboundRoute, {
          card_cvc: "123",
          account_number: "234522134",
          ssn: "1234",
          card_number: "16661"
        });
        this.response = resp.data.json
      },

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
