<script setup>
  
	import { ref } from 'vue'
	import { reactive } from 'vue'
  
  import QuestionElement from "./QuestionElement.vue"
</script>

<template>

	<div class="mainBody">
      <QuestionElement 
      	questionType=1 
        questionText="What is the name of the first program you write when testing a new language?"
      />
    
    <QuestionElement :questionType=question3Type :questionText=question1 />
    
    <QuestionElement :questionType=question2Type :questionText=question1 :choices=question1Choices />
  </div>
</template>

<style>
  .noselect {
    -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
       -khtml-user-select: none; /* Konqueror HTML */
         -moz-user-select: none; /* Old versions of Firefox */
          -ms-user-select: none; /* Internet Explorer/Edge */
              user-select: none; /* Non-prefixed version, currently supported by Chrome, Edge, Opera and Firefox */
    }
  
  .mainBody {
    width: 100%;
    height: 100%;
    margin: none;
    padding: none;
    display: flex;
    flex-direction: column;
  }
</style>