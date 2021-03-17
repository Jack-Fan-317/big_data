<template>
  <div id="weblogs-show">
    <dv-scroll-board :config="config" />
  </div>
</template>

<script>
export default {
  name: 'weblogsShow',
  data() {
        return {
            config: {},
        }
    },
    created() {
        this.$axios.get('/api/weblogsShow/').then(response => {
            this.config = response.data.data
        })
    },
}
</script>

<style>
#weblogs-show {
  width: 50%;
  box-sizing: border-box;
  margin-left: 20px;
  height: 100%;
  overflow: hidden;
}
</style>
