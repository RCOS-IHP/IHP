<script setup>
  
	import { ref } from 'vue'
	import { reactive } from 'vue'
  
  const props = defineProps({
  	questionText: String,
    questionType: Number,
    choices: Array,
    questionId: Number,
    answerIndexes: Array
	});
  
	const questionTypes = ["multiple_choice", "short_answer", "select_multiple"];
 	  
	const question = ref({
    type: questionTypes[props.questionType],
    choices: props.choices,
    id: "question" + props.questionId,
    text: props.questionText,
    answers: props.answerIndexes
  });

  
</script>

<template>
  <div class="wrapper">
  	<p> {{questionText}} </p>
    <ul v-if="question.type == 'select_multiple'">
      <div v-for="choice in question.choices">
        <input type="checkbox" :name=question.id :id=choice :value=choice>
				<label :for=choice> {{choice}} </label><br><br>
      </div>
    </ul>
    
		<input v-else-if="question.type == 'short_answer'">
    
    <form v-else-if="question.type == 'multiple_choice'">
      <div v-for="choice in question.choices">
        //TODO: Make id actually unique using question id
        <input type="radio" :name=question.id :id=choice :value=choice>
				<label :for=choice> {{choice}} </label>
      </div>
    </form>
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
  
  .wrapper {
    padding: 20px;
  }
  
  .wrapper > form {
    padding-left: 20px;
  }
  
  .wrapper > ul {
    padding-left: 20px;
  }
  
  .wrapper > input {
    margin-left: 20px;
		width: 30%;
  }
  
</style>