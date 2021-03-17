<template>
  <div id="weblog-count">
    <div class="rose-chart-title">累计web日志时间分布</div>
    <dv-charts :option="option" />
  </div>
</template>

<script>
export default {
  name: 'WeblogCount',
  data () {
    return {
      option: {}
    }
  },
  methods: {
    createData () {
      const { randomExtend } = this

      this.option = {
        title: {
            text: '剩余油量表',
            style: {
            fill: '#fff'
            }
        },
        series: [
            {
            type: 'gauge',
            data: [ { name: 'itemA', value: 55 } ],
            center: ['50%', '55%'],
            axisLabel: {
                formatter: '{value}%',
                style: {
                fill: '#fff'
                }
            },
            axisTick: {
                style: {
                stroke: '#fff'
                }
            },
            animationCurve: 'easeInOutBack'
            }
        ]
      }
    }
  }
}
</script>

<style>
#weblog-count {
  width: 30%;
  height: 100%;
  background-color: rgba(6, 30, 93, 0.5);
  border-top: 2px solid rgba(1, 153, 209, .5);
  box-sizing: border-box;
}
.rose-chart-title {
  height: 50px;
  font-weight: bold;
  text-indent: 20px;
  font-size: 20px;
  display: flex;
  align-items: center;
  border: 1px solid green;
}
.dv-charts-container {
  height: calc(100% - 50px);
}
</style>
