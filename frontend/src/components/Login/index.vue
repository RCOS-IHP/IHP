<script setup>
  
	function doRedirect(){
    window.location.href = "http://localhost:8080/login";
  }
</script>

<template>
  
  <button id="login-button" @click="doRedirect()">Login!</button>

</template>

<script>

</script>