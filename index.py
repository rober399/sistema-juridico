from flask import Flask, render_template, request, redirect, url_for,session, flash
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import webbrowser
import mysql.connector


app = Flask(__name__)

miConexion = mysql.connector.connect( host='localhost', user='root', passwd='', db='despacho' )
cur =miConexion.cursor()

app.secret_key = 'mysecretkey'


#Pagina prinsipal
@app.route('/')
def home():
    return render_template('index.html')

#Inicio

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

#Autentificasion
@app.route('/autentificacion', methods=["GET", "POST"])
def autentificacion():
  
        Nombres = request.form['Nombres']
        password = request.form['contraseña']
        cur = miConexion.cursor()
        cur.execute("SELECT * FROM administradores WHERE Nombres='" + Nombres + "' AND Contraseña='" + password +"'")
        user = cur.fetchone()
        if user is None:
            success_message = 'Contraseña o usuario incorrecto'
            flash(success_message)
            return render_template('index.html')
        else:
            session['Nombres'] = request.form['Nombres']
            return render_template('inicio.html') 



#ADMINISTRADORES
@app.route('/Registroadmin')
def Registroadmin():
    return render_template('Registroadmin.html')

@app.route('/AgregarAdmin', methods=["GET", "POST"])
def AgregarAdmin():
    if request.method == 'POST':
        dui=request.form['DUI']
        NOMBRES=request.form['NOMBRES']
        apellido=request.form['APELLIDOS']
        telefono=request.form['TELEFONO']
        direccion=request.form['DIRECCION']
        usuario=request.form['USUARIO']
        contraseña=request.form['CONTRASEÑA']
        CORREO=request.form['CORREO']
        cur = miConexion.cursor()   
        cur.execute("INSERT INTO administradores (DUI, Nombres, Apellidos, Telefono, Direccion, NombreUsuario, Contraseña, Correo) VALUES(%s, %s, %s,%s,%s,%s,%s,%s)",(dui, NOMBRES, apellido, telefono, direccion, usuario, contraseña, CORREO))
        miConexion.commit()
        session['Nombres'] = request.form['NOMBRES']
   
    return render_template('inicio.html')

@app.route('/Listadmin')
def Listadmin():
    cur =miConexion.cursor()
    cur.execute("SELECT DUI, Nombres, Apellidos, Telefono, Direccion, NombreUsuario, Contraseña FROM administradores")
    datos = cur.fetchall()
    print (datos)
    return render_template('Listadmin.html', registros = datos)

@app.route('/Editar/<string:id>')
def Editar(id):
    cur.execute("SELECT * FROM administradores WHERE DUI =%s", (id,))
    datos = cur.fetchall()
    return render_template('Editardmin.html', registros= datos[0])

@app.route('/ActualizarAdmin/<id>', methods=['POST'])
def ActualizarAdmin(id):
    if request.method ==  'POST':
        dui=request.form['DUI']
        nombre=request.form['NOMBRES']
        apellido=request.form['APELLIDOS']
        telefono=request.form['TELEFONO']
        direccion=request.form['DIRECCION']
        usuario=request.form['USUARIO']
        contraseña=request.form['CONTRASEÑA']
        correo=request.form['CORREO']
    cur.execute("""UPDATE administradores SET DUI=%s, Nombres=%s, Apellidos=%s, Telefono=%s, Direccion=%s, NombreUsuario=%s, Contraseña=%s, Correo=%s WHERE DUI=%s""",(dui, nombre, apellido, telefono, direccion, usuario, contraseña, correo, id) )
    miConexion.commit()
    return redirect(url_for('Listadmin'))

@app.route('/EliminarAdmin/<string:id>')
def EliminarAdmin(id):
    #return id
    cur.execute("DELETE FROM administradores WHERE DUI= %s",(id,))
    miConexion.commit()
    return redirect(url_for('Listadmin'))



#CLIENTES
@app.route('/Registroclientes')
def Registroclientes():

    cur =miConexion.cursor()
    cur.execute("SELECT administradores.DUI, administradores.Nombres FROM administradores")
    dat1= cur.fetchall()
    

    return render_template('Registroclientes.html', registros = dat1)


@app.route('/Agregarcliente', methods=['POST'])
def Agregarcliente():
    if request.method == 'POST':
        Dui=request.form['DUI']
        nombre=request.form['NOMBRES']
        apellido=request.form['APELLIDOS']
        telefono=request.form['TELEFONO']
        duiadmin=request.form['administradores']
        
    cur.execute("INSERT INTO cliente (Dui, Nombres, Apellidos, Telefono, DUI_Admin) VALUES(%s, %s, %s,%s,%s)",(Dui, nombre, apellido,telefono, duiadmin))
    miConexion.commit()
   
    return redirect(url_for('Registroclientes'))

@app.route('/Listaclientes')
def Listaclientes():
    cur =miConexion.cursor()
    cur.execute("SELECT * FROM cliente")
    datos = cur.fetchall()
    print (datos)
    return render_template('Listaclientes.html', registros = datos)

@app.route('/EditarCliente/<string:id>')
def EditarCliente(id):
    cur.execute("SELECT * FROM cliente WHERE Dui =%s", (id,))
    datos = cur.fetchall()
    return render_template('ActualizarCliente.html', registros= datos[0])

@app.route('/ActualizarClient/<id>', methods=['POST'])
def ActualizarClient(id):
    if request.method ==  'POST':
        Dui=request.form['DUI']
        nombre=request.form['NOMBRES']
        apellido=request.form['APELLIDOS']
        telefono=request.form['TELEFONO']
        duiadmin=request.form['DUIADMIN']
        
    cur.execute("""UPDATE cliente SET Dui=%s, Nombres=%s, Apellidos=%s, Telefono=%s, DUI_Admin=%s WHERE Dui=%s""",(Dui, nombre, apellido,telefono, duiadmin, id) )
    miConexion.commit()
    return redirect(url_for('Listaclientes'))


@app.route('/EliminarCliente/<string:id>')
def EliminarCliente(id):
    #return id
    cur.execute("DELETE FROM cliente WHERE Dui= %s",(id,))
    miConexion.commit()
    return redirect(url_for('Listaclientes'))



#SERVICIOS
@app.route('/Servicios')
def Servicios():

    cur =miConexion.cursor()
    cur.execute("SELECT administradores.DUI, administradores.Nombres FROM administradores")
    dat1= cur.fetchall()
    return render_template('Servicios.html', registros = dat1)

@app.route('/AgregarServicio', methods=['POST'])
def AgregarServicio():
    if request.method == 'POST':
        descripcion=request.form['SERVICIO']
        costo=request.form['COSTO']
        duiadmin=request.form['administradores']
        
    cur.execute("INSERT INTO servicios (DescripcionS, Costo, DUI_Admin) VALUES(%s, %s, %s)",(descripcion, costo, duiadmin))
    miConexion.commit()
    return redirect(url_for('Servicios'))

@app.route('/Listaservicios')
def Listaservicios():
    cur =miConexion.cursor()
    cur.execute("SELECT * FROM servicios")
    datos = cur.fetchall()
    print (datos)
    return render_template('Listaservicios.html', registros = datos)


@app.route('/EditarServicio/<string:id>')
def EditarServicio(id):
    cur.execute("SELECT * FROM servicios WHERE Id =%s", (id,))
    datos = cur.fetchall()
    return render_template('ActualizarServicio.html', registros= datos[0])

@app.route('/ActualizarServi/<id>', methods=['POST'])
def ActualizarServi(id):
    if request.method ==  'POST':
        descripcion=request.form['SERVICIO']
        costo=request.form['COSTO']
        duiadmin=request.form['DUI']
        
    cur.execute("""UPDATE servicios SET DescripcionS=%s, Costo=%s, Dui_Admin=%s WHERE Id=%s""",(descripcion, costo, duiadmin, id) )
    miConexion.commit()
    return redirect(url_for('Listaservicios'))


@app.route('/EliminarServicio/<string:id>')
def EliminarServicio(id):
    #return id
    cur.execute("DELETE FROM servicios WHERE Id= %s",(id,))
    miConexion.commit()
    return redirect(url_for('Listaservicios'))




   
#citas
@app.route('/Citas')
def Citas():

    cur =miConexion.cursor()
    cur.execute("SELECT administradores.DUI, administradores.Nombres FROM administradores")
    dat1= cur.fetchall()
    

   
    cur.execute("SELECT cliente.Dui, cliente.Nombres FROM cliente")
    dat2= cur.fetchall()
   
    return render_template('Registrocita.html' , registros = dat1, registros2 = dat2)   
    

@app.route('/AgregarCita', methods=['POST'])
def AgregarCita():
    if request.method == 'POST':
        fecha=request.form['CITA']
        hora=request.form['HORA']
        duicliente=request.form['cliente']
        duiadmin=request.form['administradores']
        cur.execute("INSERT INTO citas (Fecha_cita, Hora_cita, Dui_cliente, Dui_admin) VALUES(%s, %s, %s, %s)",(fecha, hora, duicliente, duiadmin))
        miConexion.commit()
        return render_template('Registrocita.html')
    

@app.route('/Listacitas')
def Listacitas():
    cur =miConexion.cursor()
    cur.execute("SELECT * FROM citas")
    datos = cur.fetchall()
    print (datos)
    return render_template('Listacitas.html', registros = datos)

@app.route('/EditarCita/<id>')
def EditarCita(id):
    cur.execute("SELECT * FROM citas WHERE ID =%s", (id,))
    datos = cur.fetchall()
    return render_template('ActualizarCita.html', registros= datos[0])

@app.route('/ActualizarCita/<id>', methods=['POST'])
def ActualizarCita(id):
    if request.method ==  'POST':
        fecha=request.form['CITA']
        hora=request.form['HORA']
        duicliente=request.form['CLIENTE']
        duiadmin=request.form['ADMIN']
        
    cur.execute("""UPDATE citas SET Fecha_cita=%s, Hora_cita=%s, Dui_cliente=%s, Dui_admin=%s  WHERE ID=%s""",(fecha, hora, duicliente, duiadmin, id) )
    miConexion.commit()
    return redirect(url_for('Listacitas'))

@app.route('/EliminarCita/<string:id>')
def EliminarCita(id):
    #return id
    cur.execute("DELETE FROM citas WHERE ID= %s",(id,))
    miConexion.commit()
    return redirect(url_for('Listacitas'))



#cliente-servicio

@app.route('/Cliser')
def Cliser():
    cur =miConexion.cursor()
    cur.execute("SELECT cliente.Dui, cliente.Nombres FROM cliente")
    dat1= cur.fetchall()
    

    cur =miConexion.cursor()
    cur.execute("SELECT servicios.Id, servicios.DescripcionS FROM servicios")
    dat2= cur.fetchall()
    return render_template('servicio_cliente.html' , registros = dat1, registros2 = dat2)
    
    

@app.route('/Agregarsv', methods=['POST'])
def Agregarsv():
    if request.method == 'POST':
        cliente=request.form['cliente']
        servicio=request.form['servicios']
        estado=request.form['PAGO']
        
        
    cur.execute("INSERT INTO servicio_cliente (Dui_cliente, Id_sevicio, Estado_pago) VALUES(%s, %s, %s)",(cliente,  servicio, estado))
    miConexion.commit()
    return redirect(url_for('Cliser'))

@app.route('/Listasv')
def Listasv():
    cur =miConexion.cursor()
    cur.execute("SELECT * FROM servicio_cliente")
    datos = cur.fetchall()
    print (datos)
    return render_template('Listasv.html', registros = datos)

@app.route('/Editarsv/<string:id>')
def Editarsv(id):
    cur.execute("SELECT * FROM servicio_cliente WHERE Id =%s", (id,))
    datos = cur.fetchall()
    return render_template('ActualizarSc.html', registros= datos[0])
    
    

@app.route('/Actualizarsc/<id>', methods=['POST'])
def Actualizarsc(id):
    if request.method ==  'POST':
        cliente=request.form['cliente']
        servicio=request.form['servicios']
        estado=request.form['PAGO']
        cur.execute("""UPDATE servicio_cliente SET Dui_cliente=%s, Id_sevicio=%s, Estado_pago=%s  WHERE ID=%s""",( cliente, servicio, estado, id) )
        miConexion.commit()
    return redirect(url_for('Listasv'))

#@app.route('/Eliminarsc/<string:id>')
#def Eliminarsc(id):
    #return id
    #cur.execute("DELETE FROM servicio_cliente WHERE Id= %s",(id,))
    #miConexion.commit()
    #return redirect(url_for('Listasv'))


#cerrar sesion

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("index.html")



# PDF

@app.route('/pdf/')
def generaPDF():
    c = canvas.Canvas('ArchivoPDF.pdf', pagesize=letter)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)
    #canvas.drawString(vertical,horizontal,'texto a imprimir')
    c.drawString(30,750,'UNIVERSIDA LUTERANA SALVADOREÑA')
    c.drawString(30,735,'REPORTE JURIDICO')



    #canvas.line(izquierdohorizontal,izquierdoVerical,derechohorizontal,derechoVertical)
    c.line(440,747,580,747)
 
    c.line(30,723,580,723) 
    #canvas.drawString(30,703,'ETIQUETA:')
    c.drawString(30,703,'ID')
    c.drawString(60,703,'Dui de cliente')
    c.drawString(300,703,'Id Servicio')
    c.drawString(400,703,'Estado de Pago')
    #canvas.line(izquierdohorizontal,izquierdoVerical,derechohorizontal,derechoVertical)
    c.line(30,700,580,700)
    
    cur.execute('SELECT * FROM servicio_cliente')
    data = cur.fetchall() 
    n=0
    incremento=0
    for row in data:
        posicionVertical=675
        n=n+incremento
        c.drawString(30,posicionVertical-n,str(row[0]))
        c.drawString(60,posicionVertical-n,str(row[1]))
        c.drawString(300,posicionVertical-n,str(row[2]))
        c.drawString(400,posicionVertical-n,str(row[3]))
        incremento=20
    c.save() 
    read_pdf = webbrowser.open_new(r'ArchivoPDF.pdf') 
   
    return redirect(url_for('Listasv'))



if __name__ == '__main__':
     app.run(port = 3000, debug = True) 


