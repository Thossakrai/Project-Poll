# Generated by Django 2.0.3 on 2018-04-04 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20180404_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answersheeta',
            name='qa1',
            field=models.PositiveSmallIntegerField(verbose_name='การหกล้มอาจทำให้กระดูกหักได้'),
        ),
        migrations.AlterField(
            model_name='answersheeta',
            name='qa2',
            field=models.PositiveSmallIntegerField(verbose_name='ถ้าท่านหกล้มศีรษะกระแทกพื้นทำให้ได้รับบาดเจ็บรุนแรงถึงขั้นเสียชีวิตได้'),
        ),
        migrations.AlterField(
            model_name='answersheeta',
            name='qa3',
            field=models.PositiveSmallIntegerField(verbose_name='หากท่านไม่จัดการสิ่งกีดขวางเกะกะทางเดินอาจทำให้ท่านพิการจากการหกล้มได้'),
        ),
        migrations.AlterField(
            model_name='answersheeta',
            name='qa4',
            field=models.PositiveSmallIntegerField(verbose_name='หากท่านไม่จัดการสิ่งแวดล้อมภายในบ้านจะทำให้ท่านหกล้มเกิดการบาดเจ็บศีรษะกระแทกพื้นและมีโอกาสเสียชีวิตได้'),
        ),
        migrations.AlterField(
            model_name='answersheeta',
            name='qa5',
            field=models.PositiveSmallIntegerField(verbose_name='หากท่านไม่ปฏิบัติท่ากายบริหารเพื่อความแข็งแรงของกล้ามเนื้อจะทำให้หกล้มศีรษะกระแทกพื้นเป็นอัมพาตได้ง่าย'),
        ),
        migrations.AlterField(
            model_name='answersheeta',
            name='qa6',
            field=models.PositiveSmallIntegerField(verbose_name='หากท่านไม่ปฏิบัติตัวตามคำแนะนำของบุคลากรทางการแพทย์ในการป้องกันการหกล้มจะทำให้ท่านหกล้มกระดูกสะโพกหัก'),
        ),
        migrations.AlterField(
            model_name='answersheetb',
            name='qb1',
            field=models.PositiveSmallIntegerField(verbose_name='ท่านเชื่อว่าการหกล้มเกิดจากการไม่จัดการสิ่งแวดล้อมภายในบ้าน'),
        ),
        migrations.AlterField(
            model_name='answersheetb',
            name='qb2',
            field=models.PositiveSmallIntegerField(verbose_name='ท่านเชื่อว่าการหกล้มเกิดจากกล้ามเนื้อไม่แข็งแรงเนื่องจากไม่ปฏิบัติท่ากายบริหาร'),
        ),
        migrations.AlterField(
            model_name='answersheetb',
            name='qb3',
            field=models.PositiveSmallIntegerField(verbose_name='พื้นห้องน้ำห้องส้วมที่บ้านเปียกอาจจะทำให้ท่านหกล้มได้ง่าย'),
        ),
        migrations.AlterField(
            model_name='answersheetb',
            name='qb4',
            field=models.PositiveSmallIntegerField(verbose_name='แสงสว่างที่บ้านไม่เพียงพอโดยเฉพาะบริเวณบันได ห้องน้ำ ทำให้เสี่ยงต่อการหกล้มได้'),
        ),
        migrations.AlterField(
            model_name='answersheetb',
            name='qb5',
            field=models.PositiveSmallIntegerField(verbose_name='การที่บ้านท่านไม่มีการจัดการสิ่งแวดล้อม เช่น ราวจับ ประตู ทางลาด ทำให้เสี่ยงต่อการหกล้มได้ง่าย'),
        ),
        migrations.AlterField(
            model_name='answersheetb',
            name='qb6',
            field=models.PositiveSmallIntegerField(verbose_name='การที่ภายในบ้านมีสิ่งกีดขวาง เกะกะทางเดิน เช่น สายไฟ ข้าวของ เครื่องใช้ทำให้เสี่ยงต่อการหกล้มได้ง่าย'),
        ),
        migrations.AlterField(
            model_name='answersheetc',
            name='qc1',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='answersheetc',
            name='qc2',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='answersheetc',
            name='qc3',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='answersheetc',
            name='qc4',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='answersheetc',
            name='qc5',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='answersheetc',
            name='qc6',
            field=models.PositiveSmallIntegerField(),
        ),
    ]