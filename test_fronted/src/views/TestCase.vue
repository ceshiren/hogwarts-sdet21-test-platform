<template>
  <v-data-table
    :headers="headers"
    :items="desserts"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>测试用例</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              新增用例
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.id"
                      label="ID"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.nodeid"
                      label="NodeId"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.remark"
                      label="备注"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                取消
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="save"
              >
                保存
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5">确认删除用例?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">取消</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">确认</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="initialize"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
</template>
<script>
  export default {
    data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'ID',
          align: 'start',
          sortable: false,
          value: 'id',
        },
        { text: 'NodeID', value: 'nodeid' },
        { text: '备注', value: 'remark' },
        { text: '操作', value: 'actions', sortable: false },
      ],
      desserts: [],
      editedIndex: -1,
      editedItem: {
        id: 0,
        nodeid: '',
        remark: '',
      },
      defaultItem: {
        id: 0,
        nodeid: '',
        remark: '',
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? '新增用例' : '编辑用例'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        // 当页面初始化的时候就发起一个获取用例的 get 请求
        this.$api.testcase.getTestcase().then((result) => {
          console.log(result)
          // 提取响应数据，赋值给 this.desserts，把数据展示在页面中
          this.desserts = result.data.msg.data
        }).catch((err) => {
          console.log(err)
        });
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      // 删除用例
      deleteItemConfirm () {
        // 调用删除接口
        // 拿到用例 id
        console.log(this.editedItem.id)
        // 调用删除接口，传入 id
        this.$api.testcase.deleteTestcase({'id': this.editedItem.id}).then((result) => {
          if (result.data.error === 0) {
            this.initialize()
          }
        }).catch((err) => {
          console.log('用例删除失败')
          console.log(err)
        });
        // this.desserts.splice(this.editedIndex, 1)
        this.closeDelete()
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      // 新增和更新用例
      save () {
        if (this.editedIndex > -1) {
          // 确定新增的逻辑在哪个分支
          console.log('this.editedIndex > -1')
          // 更新用例逻辑
          // 要更新的数据
          console.log(this.editedItem)
          // 调用更新接口，传入要更新的数据
          this.$api.testcase.updateTestcase(this.editedItem).then((result) => {           
            if (result.data.error === 0) {
              this.initialize()
            } else {
              console.log('更新用例失败')
              console.log(result)
            }
          }).catch((err) => {
            console.log(err)
          });
          // Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          // 新增用例逻辑
          console.log('else')
          // 新增用例的数据
          console.log(this.editedItem)
          this.$api.testcase.addTestcase(this.editedItem).then((result) => {
            if (result.data.error === 0) {
              this.initialize()
            } else {
              console.log('新增用例失败')
              console.log(result)
            }
          }).catch((err) => {
            console.log(err)
          });
          // this.desserts.push(this.editedItem)
        }
        this.close()
      },
    },
  }
</script>