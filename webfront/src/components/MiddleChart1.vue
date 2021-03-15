<template>
    <div class="middle-chart-1">
        <div class="cc-header">
            <dv-decoration-1 style="width:200px;height:50px;" />
            <div>日志信息</div>
            <dv-decoration-1 style="width:200px;height:50px;" />
        </div>

        <!-- <div class="cc-details">
            <div class="log_total">日志总数</div>
            <div class="card">2</div>
            <div class="card">1</div>
            <div class="card">3</div>
            <div class="card">7</div>
            <div class="card">7</div>
            <div class="card">7</div>
            <div class="card">7</div>
        </div>

        <div class="cc-main-container">
            <div class="ccmc-left">
                <div class="station-info">
                  <span>00:00~06:00</span>
                  <br>
                  <span>时段1</span>
                </div>
                <br>
                <div class="station-info">
                  <span>06:00~12:00</span>
                  <br>
                  <span>时段2</span>
                </div>
            </div>
            <div class="ccmc-middle">
                <dv-active-ring-chart :config="config" style="width:300px;height:300px"/>
            </div>
            <div class="ccmc-right">
                <div class="station-info">
                  <span>12:00~18:00</span>
                  <br>
                  <span>时段3</span>
                </div>
                <br>
                <div class="station-info">
                  <span>18:00~24:00</span>
                  <br>
                  <span>时段4</span>
                </div>
            </div>
        </div> -->
          
    </div>
</template>


<script>
export default {
  name: 'MiddleChart1',
  data () {
    return {
      config: {
        data: [
          {
            name: '收费站',
            value: 1315
          },
          {
            name: '监控中心',
            value: 415
          },
          {
            name: '道路外场',
            value: 90
          },
          {
            name: '其他',
            value: 317
          }
        ],
        color: ['#00baff', '#3de7c9', '#fff', '#ffc530', '#469f4b'],
        lineWidth: 40,
        radius: '55%',
        activeRadius: '60%'
      },

      labelConfig: {
        data: ['收费站', '监控中心', '道路外场', '其他']
      }
    }
  }
}
</script>

<style>
.middle-chart-1 {
  width: 100%;
  height: 100%;
  margin: 0px;
  padding: 0px;
  display: flex;
  flex-direction: column;
  border: 1px solid red;
}
.cc-header {
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 40px;
  color: white;
  letter-spacing: 20px;
  border: 5px solid green;
}

.cc-details {
  height: 120px;
  display: flex;
  justify-content: center;
  font-size: 32px;
  align-items: center;
  border: 1px solid red;
}
.log_total {
  color: #eee;
  margin-right: 30px;
}
.card {
  background-color: rgba(4,49,128,.6);
  color: #08e5ff;
  height: 70px;
  width: 70px;
  font-size: 45px;
  font-weight: bold;
  line-height: 70px;
  text-align: center;
  margin: 5px;
}
  
.cc-main-container {
  position: relative;
  flex: 1;
  display: flex;
  border: 1px solid red;
  height: 310px;
}
.ccmc-middle {
  width: 50%;
  height: 100%;
  border: 1px solid yellow;
  padding-left: 90px;
}
.active-ring-name {
  font-size: 20px !important;
}
    

.ccmc-left, .ccmc-right {
  width: 25%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  border: 5px solid green;
}
.ccmc-left span,.ccmc-right span {
  font-size: 30px;
  font-weight: bold;
}
.station-info {
  height: 80px;
  /* display: flex; */
  align-items: center;
}
.ccmc-left {
  align-items: flex-end;
}
.ccmc-left span {
  margin-left: 5px;
}

.ccmc-right {
  align-items: flex-start;
}
.ccmc-right span {
  margin-right: 5px;
}
</style>