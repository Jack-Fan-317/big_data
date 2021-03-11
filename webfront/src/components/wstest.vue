<template>
    <div>
        <div id="input-send">
            <textarea placeholder="请输入内容" v-model="sendmsg"></textarea>
            <button>发送信息</button>
        </div>
    </div>
</template>

<script type="text/javascript">
export default {
    name: "test",
    data() {
        return {
            sendmsg:"",
        }
    },
    mounted() {
        this.initWebSocket()
    },
    methods: {
        initWebSocket() {
            let wsuri = 'ws://127.0.0.1:8000/chat/lobby';
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
            // this.ws.send(msg)
        },

        websocketOnMessage(e) {
            //获取websocket推送的数据
            // let msg = e.data
            // console.log(msg)
            console.log(e.data)
            let message = JSON.parse(e.data)
            if (message.code == 100) {
                console.log("fjk")
            }
        },

        websocketOnOpen(e) {
            console.log(e)
            let enterroom = {
                code:100,
                msg:'hahaha'
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

    // created() {
    //     this.$axios.get('/api/city1/').then(response => {
    //         this.config1 = response.data.data
    //     })
    //     this.$axios.get('/api/city2/').then(response => {
    //         this.config2 = response.data.data
    //     })
    // },
};
</script>

<style>
html,body{
    margin: 0;
    padding: 0;
}

</style>