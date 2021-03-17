<template>
  <div id="weblogs-total">
    <div class="water-level-chart-title">日志累计采集数量情况</div>

    <div class="water-level-chart-details">
      <p>累计采集</p>
      <span>{{data}}</span>
      <p>条数据</p>
    </div>

    <div class="chart-container">
      <dv-water-level-pond :config="config" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'weblogsTotal',
  data () {
    return {
      config: {
        data: [45],
        shape: 'round',
        waveHeight: 25,
        waveNum: 3,
        waveOpacity: 0.6
      },
      data: ''
    }
  },
  created() {
      this.$axios.get('/api/weblogsTotal/').then(response => {
          this.data = response.data.data
      })
  },
}
</script>

<style>
#weblogs-total {
  width: 20%;
  box-sizing: border-box;
  margin-left: 20px;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, .5);
  display: flex;
  flex-direction: column;
}
.water-level-chart-title {
  font-weight: bold;
  height: 50px;
  display: flex;
  align-items: center;
  font-size: 20px;
  justify-content: center;
}
.water-level-chart-details {
  height: 15%;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}
.water-level-chart-details p {
  font-size: 13px;
}
.water-level-chart-details span {
  font-size: 35px;
  font-weight: bold;
  color: #58a1ff;
  margin: 0 5px;
  text-align: center;

}
.chart-container {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
.dv-water-pond-level {
  max-width: 70%;
  width: 200px;
  height: 200px;
  border: 10px solid #19c3eb;
  border-radius: 50%;
  padding-right: 7px;
  padding-bottom: 7px;
}
.dv-water-pond-level  ellipse {
  stroke: transparent !important;
}
.dv-water-pond-level  text {
  font-size: 40px;
}
</style>
