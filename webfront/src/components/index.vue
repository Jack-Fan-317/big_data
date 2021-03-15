<template>
    <div>
        <dv-full-screen-container>
            <top-header />
                <dv-border-box-1 class="main-container">
                    <dv-border-box-3 class="left-chart-container">
                        <Left-Chart-1 />
                        <Left-Chart-2 />
                    </dv-border-box-3>
                </dv-border-box-1>
        </dv-full-screen-container>
    </div>
</template>

<script>
import topHeader from './topHeader'
import LeftChart1 from './LeftChart1'
import LeftChart2 from './LeftChart2'

export default {
    name: 'index',
    components: {
        topHeader,
        LeftChart1,
        LeftChart2,
    },
    data () {
        return {}
    },
    methods: {}
}
</script>

<style>
html,body{
    margin: 0;
    padding: 0;
}
#dv-full-screen-container {
    background: url('../assets/bg.png');
    background-size: cover;
    box-shadow: 0 0 3px blue;
    display: flex;
    flex-direction: column;
}
.main-container {
    height :calc(100% - 80px);
    border: 1px solid green;
}
.left-chart-container {
    width: 22%;
    padding: 10px;
    box-sizing: border-box;
}
</style>
