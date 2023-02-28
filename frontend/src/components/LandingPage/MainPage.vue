<script setup>
  
	import { ref } from 'vue'
	import { reactive } from 'vue'
  import Header from "./Header.vue"
  import LoginField from "./LoginField.vue"
</script>

<template>
  
  <Header/>
    
  <LoginField/>

</template>

<style>
  body {
    background-color: #FFFFFF;
    margin: 0;
  }
  
  .loginContainer {
    position: absolute;
    
    right: 20px;
    margin-top: 20px;
  }
  
  .noselect {
    -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
       -khtml-user-select: none; /* Konqueror HTML */
         -moz-user-select: none; /* Old versions of Firefox */
          -ms-user-select: none; /* Internet Explorer/Edge */
              user-select: none; /* Non-prefixed version, currently supported by Chrome, Edge, Opera and Firefox */
    }
</style>