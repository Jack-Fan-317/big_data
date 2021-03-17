<template>
  <div>
        <h2>柱形图-就业行业</h2>
        <div class="chart" id="container">图标</div>
  </div>
</template>
<script>
//先导入charts
import Charts from '@jiaminghi/charts'
export default {
  
  data () {
    return {
    };
  },
  created() {
      this.$axios.get('/api/timeItems/').then(response => {
          const container = document.getElementById('container')
          const myChart = new Charts(container)
          let row_data = response.data.data
          console.log(row_data)
          var option={
                title: row_data.title,
                xAxis: row_data.xAxis,
                yAxis: row_data.yAxis,
                series: row_data.series
            }
          myChart.setOption(option)
        
        })
      
        
  },
  
          
  mounted(){
  },
  methods:{

  
  
  }
}
</script>
<style>
  .chart{
    height: 2000px;
    width: 2000px;
    margin-left: 225px;
  }
  
  h2{
    height: 400px;
    color: #123;
    font-size: 90px;
    font-weight: 400;
    text-align: center;
    line-height: 48px;
  }
</style>