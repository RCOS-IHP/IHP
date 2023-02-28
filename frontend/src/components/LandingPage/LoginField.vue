<script setup>
  import { ref } from 'vue'
	import { reactive } from 'vue'
  
	let loginRequired = ref(false);
  	
  const userInfo = ref({ 
    name: "Luke", 
    year: "Freshman",
    classes: ref([ "Math", "RCOS", "FoCS" ])
  });
  

</script>

<template>
  
	<div :class=" ['loginContainer']">
    <div v-if="loginRequired" :id="['loginField']">
      LOGIN
      
      <button @click="loginRequired = false;">Log In</button>
    </div>
    <div v-else>
      <div>
        Welcome {{userInfo.name}}!
      </div>
      
      <br>  
      
      <div>
        Year: {{userInfo.year}}
      </div>
      
      <br>
      <div>
        Current Classes: 
      </div>
      <div v-for="className in userInfo.classes" :key="className">
				<li>{{ className }}</li>
      </div>
      
      <button @click="loginRequired = true;">Log Out</button>
    </div>
  </div>
  
</template>

<style>  
  .loginContainer {
    width: 300px;
    height: 400px;
    background-color: #dfe2e0;
    
    display: flex;
    flex-direction: row;
    justify-content: center;
    border-radius: 10px;
  }
  
  .loginContainer > * {
    margin: 50px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
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