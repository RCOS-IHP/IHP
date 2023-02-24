<script setup>
  
	import { ref } from 'vue'
	import { reactive } from 'vue'
  

  let showHeader = ref(true);
  let loginRequired = ref(true);
  
  const headerLinkClass = ['headerLink', 'noselect'];
  
  const userInfo = ref({ 
    name: "Luke", 
    year: "Freshman",
    classes: ref([ "Math", "RCOS" ])
  });
    
  const headerLinks = ref([
    { id: "homeLink", text: 'Home', click: "", class: headerLinkClass },
    { id: "divider", text: '|', click: "", class: "noselect" },
    { id: "classLink", text: 'Class', click: "",class: headerLinkClass },
    { id: "divider", text: '|', click: "", class: "noselect" },
    { id: "assignmentLinks", text: 'Assignments', click:"", class: headerLinkClass },
    { id: "divider", text: '|', click: "", class: "noselect" },
    { id: "linkD", text: 'Link D', click: "",class: headerLinkClass },
    { id: "divider", text: '|', click: "", class: "noselect" },
    { id: "linkE", text: 'Link E', click:"", class: headerLinkClass }
  ]);
  
</script>

<template>
  
  <div v-if="showHeader" :id="['header']" :class="['header']"> 
    <div v-for="link in headerLinks" :key="link.id" @click="link.click" :class="link.class">
      {{ link.text }}
    </div>
  </div>
  
  <div :class="['loginContainer']">
    <div v-if="loginRequired" :id="['loginField']">
      LOGIN
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
				&nbsp;&nbsp;&nbsp;&nbsp;{{ className }}
      </div>
      
    </div>
  </div>
  
  <button @click="loginRequired = !loginRequired;">toggle</button>
</template>

<style>
  body {
    background-color: #FFFFFF;
    margin: 0;
  }
  
  .header {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 20px;
    background-color: #595fd9;
    flex-wrap: none;
    position: sticky;
    
    color: #DFE2E0;
  }
  
  .header > .headerLink {
    cursor: pointer; 
  	overflow: hidden;
    white-space: nowrap;
  }
  
  .loginContainer {
    position: absolute;
    
    right: 20px;
    margin-top: 20px;
    width: 300px;
    height: 400px;
    background-color: #dfe2e0;
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