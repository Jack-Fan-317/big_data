<template>
  <div id="topic-board">
    <div class="ranking-board-title">话题TOP50</div>
    <dv-scroll-ranking-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'topicBoard',
  data() {
        return {
            config: {},
        }
    },
    created() {
        this.$axios.get('/api/webcount/').then(response => {
            this.config = response.data.data
        })
    },
}
</script>

<style>
#topic-board {
  width: 20%;
  box-shadow: 0 0 3px blue;
  display: flex;
  flex-direction: column;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, .5);
  box-sizing: border-box;
  padding: 0px 30px;
  border: 1px solid red;
}
.ranking-board-title {
  font-weight: bold;
  height: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 15px;
  /* border: 1px solid red; */
  padding-top:20px;
  letter-spacing: 4px;
}
.dv-scroll-ranking-board {
  flex: 1;
}
</style>
