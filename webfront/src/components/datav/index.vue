<template>
    <div id="data-view">
        <dv-full-screen-container>
            <top-header />
            <div class="main-content">
                <digital-flop />
                <div class="block-left-right-content">
                    <weblogs-topic />
                    <div class="block-top-bottom-content">
                        <div class="block-top-content">
                            <time-distrib />
                            <weblogs-total />
                            <weblogs-show />
                        </div>
                        <time-items />
                    </div>
                </div>
            </div>
        </dv-full-screen-container>
    </div>
</template>

<script>
import topHeader from './topHeader'
import digitalFlop from './digitalFlop'
import weblogsTopic from './weblogsTopic'
import weblogsTotal from './weblogsTotal'
import weblogsShow from './weblogsShow'
import timeDistrib from './timeDistrib'
import timeItems from './timeItems'


export default {
    name: 'DataView',
    components: {
        topHeader,
        digitalFlop,
        weblogsTopic,
        weblogsTotal,
        weblogsShow,
        timeDistrib,
        timeItems
    },
    data () {
        return {}
    },
    methods: {}
}
</script>

<style>
#data-view {
  width: 100%;
  height: 100%;
  background-color: #030409;
  color: #fff;
}
#dv-full-screen-container {
    background: url('../img/bg.png');
    background-size: cover;
    box-shadow: 0 0 3px blue;
    display: flex;
    flex-direction: column;
}
.main-content {
    flex: 1;
    display: flex;
    flex-direction: column;
}
.block-left-right-content {
    flex: 1;
    display: flex;
    margin-top: 20px;
    height: 600px;
}
.block-top-bottom-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    padding-left: 20px;
  }
.block-top-content {
    height: 55%;
    display: flex;
    flex-grow: 0;
    box-sizing: border-box;
    padding-bottom: 20px;
}
</style>