<template>
    <div id="data-view">
        <dv-full-screen-container>
            <top-header />
            <div class="main-content" style="border: 1px solid green;">
                <digital-flop />
                <div class="block-left-right-content" style="border: 1px solid green;"><!-- 左边一列 -->
                    <topic-board />
                    <div class="block-top-bottom-content" style="border: 1px solid white;">
                        <div class="block-top-content" style="border: 1px solid white;">
                            <rose-chart />
                            <!-- <weblog-count/> -->
                            <water-level-chart />
                            <wblogs-board />
                        </div>
                        <cards />
                    </div>
                </div>
            </div>
        </dv-full-screen-container>
    </div>
</template>

<script>
import topHeader from './topHeader'
import digitalFlop from './digitalFlop'
import topicBoard from './topicBoard'
import roseChart from './roseChart'
import waterLevelChart from './waterLevelChart'
import wblogsBoard from './wblogsBoard'
import cards from './cards'
// import weblogCount from './weblogCount'

export default {
    name: 'DataView',
    components: {
        topHeader,
        digitalFlop,
        topicBoard,
        roseChart,
        waterLevelChart,
        wblogsBoard,
        cards,
        // weblogCount
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
