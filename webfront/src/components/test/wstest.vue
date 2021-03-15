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
    name: "wstest",
    data() {
        return {
            config1: {},
            config2: {},
        }
    },
    mounted() {
        this.initWebSocket()
    },
    methods: {
        initWebSocket() {
            let wsuri = 'ws://127.0.0.1:8000/city/city1';
            // 连接服务器
            this.ws = new WebSocket(wsuri);
            // 指定事件回调
            this.ws.onmessage = this.websocketOnMessage;
            this.ws.onopen = this.websocketOnOpen;
            this.ws.onerror = this.websocketOnError;
            this.ws.onclose = this.websocketClose;
        }, 
        // 发送消息
        sendWebSocketMsg(msg) {
            this.ws.send(JSON.stringify(msg))
        },

        websocketOnMessage(e) {
            //获取websocket推送的数据
            // let msg = e.data
            // console.log(msg)
            // console.log(e.data)
            let message = JSON.parse(e.data)
            // if (message.code == 100) {
            //     console.log("fjk")
            // }
            // console.log(message)
        },

        websocketOnOpen(e) {
            console.log(e)
            let enterroom = {
                code:100,
                msg:'fjk'
            }
            this.sendWebSocketMsg(enterroom)
            // console.log('连接 websocket 成功')
        },
        
        // 连接失败时重新连接
        websocketOnError(e) {
            // this.initWebSocket()
            console.log(e)
        },
        // 断开链接后报错
        websocketClose(e) {
            console.log('断开连接', e.code + " " + e.reason + " " + e.wasClean);
            //this.initWebSocket() //断开后重新连接
        },
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