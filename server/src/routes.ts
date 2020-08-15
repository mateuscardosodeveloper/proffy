import express from 'express'
import ClassesController from './controllers/ClassesController'
import ConnectionsControler from './controllers/ConnectionsControler'

const routes = express.Router()
const classesControllers = new ClassesController()
const connectionsControler = new ConnectionsControler


routes.get('/classes', classesControllers.index)
routes.post('/classes', classesControllers.create)

routes.get('/connections', connectionsControler.index)
routes.post('/connections', connectionsControler.create)

export default routes

