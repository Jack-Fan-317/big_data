<template>
    <div id="time-items">
        <div class="time-item">
            <div class="item-header">
                <div class="item-header-left">时段 00:00~06:00</div>
                <div class="item-header-right">01</div>
            </div>
            <div class="chart" id="container1"></div>
        </div>
        <div class="time-item">
            <div class="item-header">
                <div class="item-header-left">时段 06:00~12:00</div>
                <div class="item-header-right">02</div>
            </div>
            <div class="chart" id="container2"></div>
        </div>
        <div class="time-item">
            <div class="item-header">
                <div class="item-header-left">时段 12:00~18:00</div>
                <div class="item-header-right">03</div>
            </div>
            <div class="chart" id="container3"></div>
        </div>
        <div class="time-item">
            <div class="item-header">
                <div class="item-header-left">时段 18:00~24:00</div>
                <div class="item-header-right">04</div>
            </div>
            <div class="chart" id="container4"></div>
        </div>
    </div>
</template>

<script>
import Charts from '@jiaminghi/charts'
export default {
    name: 'timeItems',
    data () {
        return {

        }
    },
    created() {
        this.$axios.get('/api/timeItems/').then(response => {
            const container1 = document.getElementById('container1')
            const container2 = document.getElementById('container2')
            const container3 = document.getElementById('container3')
            const container4 = document.getElementById('container4')
            const myChart1 = new Charts(container1)
            const myChart2 = new Charts(container2)
            const myChart3 = new Charts(container3)
            const myChart4 = new Charts(container4)
            let row_data1 = response.data.data1
            let row_data2 = response.data.data2
            let row_data3 = response.data.data3
            let row_data4 = response.data.data4
            var option1 = {
                title: row_data1.title,
                xAxis: row_data1.xAxis,
                yAxis: row_data1.yAxis,
                series: row_data1.series
            }
            var option2 = {
                title: row_data2.title,
                xAxis: row_data2.xAxis,
                yAxis: row_data2.yAxis,
                series: row_data2.series
            }
            var option3 = {
                title: row_data3.title,
                xAxis: row_data3.xAxis,
                yAxis: row_data3.yAxis,
                series: row_data3.series
            }
            var option4 = {
                title: row_data4.title,
                xAxis: row_data4.xAxis,
                yAxis: row_data4.yAxis,
                series: row_data4.series
            }
            myChart1.setOption(option1)
            myChart2.setOption(option2)
            myChart3.setOption(option3)
            myChart4.setOption(option4)
        })
    },
    mounted(){
        // (function(){
        // //下面和eacharts差不多
        //     const container1 = document.getElementById('container1')
        //     const container2 = document.getElementById('container2')
        //     const container3 = document.getElementById('container3')
        //     const container4 = document.getElementById('container4')
        //     const myChart1 = new Charts(container1)
        //     const myChart2 = new Charts(container2)
        //     const myChart3 = new Charts(container3)
        //     const myChart4 = new Charts(container4)
        //     var option1={
        //         title: {
        //             text: '日志量',
        //             style:{ //标题默认样式
        //                 fill: '#eee',
        //                 fontSize: 17,
        //                 fontWeight: '400',
        //                 textAlign: 'center',
        //                 textBaseline: 'bottom',
        //             },
        //         },
        //         xAxis: {
        //             name: '时',
        //             data: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         yAxis: {
        //             name: '条',
        //             data: 'value',
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         series: [
        //             {
        //                 data: [1120, 2223, 1110, 2110, 3510, 4110],
        //                 type: 'bar',
        //                 gradient: {
        //                     color: ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
        //                 },
        //                 barStyle: {
        //                     stroke: '#fb7293'
        //                 }
        //             }
        //         ]
        //     }
        //     var option2={
        //         title: {
        //             text: '日志量',
        //             style:{ //标题默认样式
        //                 fill: '#eee',
        //                 fontSize: 17,
        //                 fontWeight: '400',
        //                 textAlign: 'center',
        //                 textBaseline: 'bottom',
        //             },
        //         },
        //         xAxis: {
        //             name: '时',
        //             data: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         yAxis: {
        //             name: '条',
        //             data: 'value',
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         series: [
        //             {
        //                 data: [1120, 2223, 1110, 2110, 3510, 4110],
        //                 type: 'bar',
        //                 gradient: {
        //                     color: ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
        //                 },
        //                 barStyle: {
        //                     stroke: '#fb7293'
        //                 }
        //             }
        //         ]
        //     }
        //     var option3={
        //         title: {
        //             text: '日志量',
        //             style:{ //标题默认样式
        //                 fill: '#eee',
        //                 fontSize: 17,
        //                 fontWeight: '400',
        //                 textAlign: 'center',
        //                 textBaseline: 'bottom',
        //             },
        //         },
        //         xAxis: {
        //             name: '时',
        //             data: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         yAxis: {
        //             name: '条',
        //             data: 'value',
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         series: [
        //             {
        //                 data: [1120, 2223, 1110, 2110, 3510, 4110],
        //                 type: 'bar',
        //                 gradient: {
        //                     color: ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
        //                 },
        //                 barStyle: {
        //                     stroke: '#fb7293'
        //                 }
        //             }
        //         ]
        //     }
        //     var option4={
        //         title: {
        //             text: '日志量',
        //             style:{ //标题默认样式
        //                 fill: '#eee',
        //                 fontSize: 17,
        //                 fontWeight: '400',
        //                 textAlign: 'center',
        //                 textBaseline: 'bottom',
        //             },
        //         },
        //         xAxis: {
        //             name: '时',
        //             data: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6'],
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         yAxis: {
        //             name: '条',
        //             data: 'value',
        //             nameTextStyle: {
        //                 fill: '#fff',
        //                 fontSize: 10
        //             },
        //             axisLabel:{
        //                 style: {
        //                     fill: '#fff',
        //                     fontSize: 10,
        //                     rotate: 0
        //                 }
        //             },
        //         },
        //         series: [
        //             {
        //                 data: [1120, 2223, 1110, 2110, 3510, 4110],
        //                 type: 'bar',
        //                 gradient: {
        //                     color: ['rgba(251, 114, 147, .6)', 'rgba(251, 114, 147, .1)']
        //                 },
        //                 barStyle: {
        //                     stroke: '#fb7293'
        //                 }
        //             }
        //         ]
        //     }
        //     myChart1.setOption(option1)
        //     myChart2.setOption(option2)
        //     myChart3.setOption(option3)
        //     myChart4.setOption(option4)
        // })()
  },
}
</script>

<style>
#time-items {
    display: flex;
    justify-content: space-between;
    height: 45%;
}
.time-item {
    background-color: rgba(6, 30, 93, 0.5);
    border-top: 2px solid rgba(1, 153, 209, .5);
    width: 24%;
    display: flex;
    flex-direction: column;
}
.item-header {
  display: flex;
  height: 20%;
  align-items: center;
  justify-content: space-between;
}
.item-header-left {
  font-size: 18px;
  font-weight: bold;
  padding-left: 20px;
}
.item-header-right {
  padding-right: 20px;
  font-size: 40px;
  color: #03d3ec;
}
.chart {
    height: 100%;
    padding-left: 10px;
}

</style>
