<template>
    <div id="top-header">
        <dv-decoration-8 class="header-left-decoration" />
        <dv-decoration-5 class="header-center-decoration" />
        <dv-decoration-8 class="header-right-decoration" :reverse="true" />
        <div class="center-title">Hadoop日志数据分析系统</div>
    </div>
</template>

<script>
export default {
  name: 'TopHeader'
}
</script>

<style>
#top-header {
    position: relative;
    width: 100%;
    height: 100px;
    display: flex;
    justify-content: space-between;
    flex-shrink: 0;
    border: 1px solid red;
}

.header-center-decoration {
    width: 40%;
    height: 80px;
    margin-top: 30px;
}

.header-left-decoration, .header-right-decoration {
    width: 25%;
    height: 70px;
}

.center-title {
    position: absolute;
    font-size: 30px;
    font-weight: bold;
    left: 50%;
    top: 15px;
    transform: translateX(-50%);
    color: #eee;
    letter-spacing: 5px;
}
</style>