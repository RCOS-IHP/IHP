<script setup>
  import { ref } from 'vue'
	import { reactive } from 'vue'
  
	let loginRequired = ref(false);
  let classesShown = ref(true);
  const userInfo = ref({ 
    name: "Luke", 
    year: "Freshman",
    classes: ref([ "Math", "RCOS", "FoCS" ])
  });
  
</script>

<template>
	<div :class="['loginContainer']">
    <div v-if="loginRequired" :id="['loginField']">
      First Time User?
      <button> Sign Up </button>
      
      Already Have an Account?      
      <button @click="loginRequired = false;">Log In</button>
    </div>
    <div v-else>
      <div>
        Welcome {{userInfo.name}}!
      </div>
            
      <div>
        {{userInfo.year}}
      </div>
        
      <div class="dropdown">
        <div class="noselect hover" @click="classesShown = !classesShown;"> Current Classes: </div>
        <div v-if="classesShown" v-for="className in userInfo.classes" :key="className">
					<div class="hover" @click="">{{ className }}</div>
      	</div>
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
  
  .loginContainer > div {
    margin: 50px;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  
  .loginContainer > div > button {
    height: 50px;
    background-color: #587D71;
    border-radius: 5px;
    border: none;
    color: #FFFFFF;
    
    cursor: pointer;
  }
  
  .hover {
    cursor: pointer;
  }
  
  .noselect {
    -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
       -khtml-user-select: none; /* Konqueror HTML */
         -moz-user-select: none; /* Old versions of Firefox */
          -ms-user-select: none; /* Internet Explorer/Edge */
              user-select: none; /* Non-prefixed version, currently supported by Chrome, Edge, Opera and Firefox */
    }
  
  .dropdown {
    border-left: 2px solid #0E1116;
    padding-left: 5px;
    margin-left: -5px;
  }
  
  .dropdown > div > div {
    padding-left: 15px;
  }
</style>