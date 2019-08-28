<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-center">
        <h4>Lista de libros</h4>
        <div class="col-md-12">
          <div class="col-md-4">

          </div>
          <div class="col-md-8">
            <b-table striped hover :item="books" :fields="fields">

            </b-table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    data () {
      return {
        fields: [
          { key: 'title', label: 'Titulo'},
          { key: 'stock', label: 'Disponiblidad'},
          { key: 'price', label: 'Precio'},
          { key: 'accions'}
        ],
        books: []
      }
    },
    methods:{
      getBooks (){
        const path = 'http://0.0.0.0:8000/api_scraper/books'
        axios.get(path).then((response) =>{
          this.books = response.data
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    created(){
      this.getBooks()
    }
  }
</script>


<style lang="css" scoped>
</style>
