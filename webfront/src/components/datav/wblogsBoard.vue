<template>
  <div id="weblogs-board">
    <dv-scroll-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'weblogsBoard',
  data() {
        return {
            config: {},
        }
    },
    created() {
        this.$axios.get('/api/weblogs/').then(response => {
            this.config = response.data.data
        })
    },
}
</script>

<style>
#weblogs-board {
  width: 50%;
  box-sizing: border-box;
  margin-left: 20px;
  height: 100%;
  overflow: hidden;
}
</style>
