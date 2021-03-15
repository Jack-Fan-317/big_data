<template>
  <div id="app">
    <router-view />
    <!-- <div>
        <dv-full-screen-container>
          <dv-border-box-1 class="main-container">
            <div class="main-header">
              <dv-decoration-8 class="header-left-decoration" />
              <dv-decoration-5 class="header-center-decoration" />
              <dv-decoration-8 class="header-right-decoration" :reverse="true" />
              <div class="mh-middle">Hadoop日志数据分析系统</div>
            </div>
            <dv-border-box-3 class="left-chart-container">
              <router-view name="LeftChart_router"></router-view>
              <left-chart />
              <router-view name="LeftChart2_router"></router-view>
            </dv-border-box-3>
            <dv-border-box-3 class="middle-chart-container">
              <router-view name="MiddleChart1_router"></router-view>
            </dv-border-box-3>
          </dv-border-box-1>
        
        </dv-full-screen-container>
    </div> -->
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
/* html,body{
    margin: 0;
    padding: 0;
}
#dv-full-screen-container {
    background: url('./assets/bg.png');
    background-size: 100% 100%;
    box-shadow: 0 0 3px blue;
    display: flex;
    flex-direction: column;
}
.main-header {
    height: 80px;
    display: flex;
    justify-content: center;
    align-items: center; 
    border: 1px solid red;
}
.mh-middle {
    font-size: 30px;
    color: #eee;
    letter-spacing: 10px;
    border: 1px solid red;
}
.main-header p {
  height: 80px;
  
}
.main-container {
    height: 100%;
}
.left-chart-container {
    width: 22%;
    padding: 10px;
    box-sizing: border-box;
}
.middle-chart-container{
    height: 500px;
    border: 1px solid yellow;
} */
</style>
