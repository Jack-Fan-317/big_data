<template>
  <div id="time-distrib">
    <div class="time-distrib-title">累计web日志时间分布</div>
    <dv-capsule-chart :config="config" id="count-container"/>
  </div>
</template>

<script>
import Charts from '@jiaminghi/charts'
export default {
  name: "timeDistrib",
  data() {
    return {
      config: {},
    }
  },
  created() {
    this.$axios.get('/api/timeDistrib/').then(response => {
      this.config = response.data.data
    })
  },
  mounted(){
  }
};
</script>

<style>
#time-distrib {
  width: 30%;
  height: 100%;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, 0.5);
  box-sizing: border-box;
}
.time-distrib-title {
  height: 50px;
  font-weight: bold;
  text-indent: 20px;
  font-size: 20px;
  display: flex;
  align-items: center;

}
.dv-charts-container {
  height: calc(100% - 50px);
}
#count-container {
  height: calc(100% - 50px);
  padding-top: 10px;
}

</style>
