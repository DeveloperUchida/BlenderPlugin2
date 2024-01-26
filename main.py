import bpy
import random

# グローバル変数
WIDTH = 10  # 地形の幅
LENGTH = 10  # 地形の長さ
MAX_HEIGHT = 5  # 地形の最大高さ

# 関数定義
def generate_terrain():
    verts = []
    faces = []

    # 頂点生成
    for x in range(WIDTH):
        for y in range(LENGTH):
            verts.append((x, y, random.uniform(0, MAX_HEIGHT)))

    # 面生成
    for x in range(WIDTH - 1):
        for y in range(LENGTH - 1):
            index = x * LENGTH + y
            faces.append((index, index + LENGTH, index + LENGTH + 1, index + 1))

    # メッシュ生成
    mesh = bpy.data.meshes.new(name="TerrainMesh")
    mesh.from_pydata(verts, [], faces)
    mesh.update()

    # オブジェクト生成
    obj = bpy.data.objects.new("Terrain", mesh)
    bpy.context.collection.objects.link(obj)

# メイン処理
if __name__ == "__main__":
    generate_terrain()
