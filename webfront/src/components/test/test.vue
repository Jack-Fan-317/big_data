<template>
    <div>
        <dv-full-screen-container>
            <dv-border-box-11 title="大数据日志分析系统"></dv-border-box-11>
        </dv-full-screen-container>
        <div class="col-md-6">
                <div>
                    <h2 id="origin_title">数据展示</h2>
                </div>
                <!-- <div class="origin_chart"> -->
                    <div style="height:400px;">
                        <div style="height: 100%; width: 100%;background: rgb(41,44,51);">
                            <!-- 轮播图 -->
                            <dv-scroll-board :config="config1" style="width:100%;height:100%;"/>
                        </div>
                    </div>
                <!-- </div> -->
            </div>
        <!-- 数据处理 -->
            <div class="col-md-6">
                <div>
                    <h2 id="process_title">前100名热榜</h2>
                </div>
                <!-- <div class="origin_chart"> -->
                    <div style="height:400px;">
                        <div style="height: 100%; width: 100%;background: rgb(41,44,51);">
                            <!-- 轮播图 -->
                            <dv-scroll-ranking-board :config="config2" style="width:100%;height:100%;"/>
                        </div>
                    </div>
                <!-- </div> -->
            </div>
    </div>
</template>

<script type="text/javascript">
export default {
    name: "test",
    data() {
        return {
            config1: {},
            config2: {},
        }
    },
    created() {
        this.$axios.get('/api/city/city1/').then(response => {
            this.config1 = response.data.data
        })
        this.$axios.get('/api/city/city2/').then(response => {
            this.config2 = response.data.data
        })
    },
};
</script>

<style>
html,body{
    margin: 0;
    padding: 0;
}

</style>