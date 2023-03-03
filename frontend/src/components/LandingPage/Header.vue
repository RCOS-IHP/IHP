<script setup>
  
	import { ref } from 'vue'
	import { reactive } from 'vue'

  let showHeader = ref(true);
  let loginRequired = ref(true);
  
  const headerLinkClass = ['headerLink', 'noselect'];
      
  const headerLinks = ref([
    { id: "homeLink", text: 'Home', click: "link", class: headerLinkClass },
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
    <div v-for="link in headerLinks" :key="link.id" :class="link.class">
      <router-link v-if="!!link.click">
        {{link.text}}
      </router-link>
      <div v-else>
      	{{ link.text }}
      </div>
    </div>
    
    
  </div>

</template>

<style>
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
  
  .noselect {
    -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
       -khtml-user-select: none; /* Konqueror HTML */
         -moz-user-select: none; /* Old versions of Firefox */
          -ms-user-select: none; /* Internet Explorer/Edge */
              user-select: none; /* Non-prefixed version, currently supported by Chrome, Edge, Opera and Firefox */
    }
</style>